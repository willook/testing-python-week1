from unittest.mock import patch


def test_contains_profanity_true_cases(profanity_list):
    """욕설 포함 여부 테스트"""
    # given
    from app.validators.profanity_validator import ProfanityValidator

    validator = ProfanityValidator(profanity_list)
    text_list = [
        "경기 진짜 파인애플피자처럼 하네.",
        "오늘 수비 그냥 민트초코네",
        "이럴거면 파인애플 피자나 먹을걸",
        "민트초코 좋아 민트초코 좋아 민트초코 좋아",
    ]

    # when
    results = []
    for text in text_list:
        results.append(validator.contains_profanity(text))

    # then
    assert all(results)


def test_contains_profanity_false_cases(profanity_list):
    """욕설 포함 여부 테스트"""
    # given
    from app.validators.profanity_validator import ProfanityValidator

    validator = ProfanityValidator(profanity_list)
    text_list = [
        "정상적인 문장입니다.",
        "안녕하세요.",
        "오늘 야구 경기 재밌다.",
    ]

    # when
    results = []
    for text in text_list:
        results.append(validator.contains_profanity(text))

    # then
    assert not any(results)


def test_profanity_list_from_mock_admin(admin_profanity_list):
    """관리자 서비스에서 욕설 목록을 가져오는지 테스트, mock 사용"""
    # given
    from app.validators.profanity_validator import ProfanityValidator

    with patch(
        "app.services.admin.get_profanity_list_from_admin_service",
        return_value=admin_profanity_list,
    ):
        from app.services.admin import get_profanity_list_from_admin_service

        profanity_list = get_profanity_list_from_admin_service()
        validator = ProfanityValidator(profanity_list)

        text_list = [
            "오늘 경기 가지무침이네.",
            "오늘 수비 솔의눈이네",
            "이럴거면 데자와나 먹을걸",
        ]

        results = [validator.contains_profanity(text) for text in text_list]

        assert all(results)


def test_profanity_list_from_admin():
    """관리자 서비스에서 욕설 목록을 가져오는지 테스트, mock 미사용"""
    # given
    from app.services.admin import get_profanity_list_from_admin_service
    from app.validators.profanity_validator import ProfanityValidator

    profanity_list = get_profanity_list_from_admin_service()
    validator = ProfanityValidator(profanity_list)

    text_list = [
        "오늘 경기 가지무침이네.",
        "오늘 수비 솔의눈이네",
        "이럴거면 데자와나 먹을걸",
    ]

    results = [validator.contains_profanity(text) for text in text_list]

    assert all(results)
