from argparse import ArgumentParser

from app.validators.profanity_validator import ProfanityValidator

parser = ArgumentParser()
parser.add_argument(
    "--title",
    type=str,
    default="안녕하세요",
    help="게시글 제목",
)
parser.add_argument(
    "--content",
    type=str,
    default="야구를 아주 파인애플피자같이 하네",
    help="게시글 내용",
)


def main(title: str, content: str):
    # 욕설 검증기 정의
    profanity_list = ["파인애플피자", "민트초코"]
    profanity_validator = ProfanityValidator(profanity_list)

    # 게시글 검증
    is_valid = profanity_validator.contains_profanity(
        title
    ) or profanity_validator.contains_profanity(content)
    print(f"게시글 제목: {title}")
    print(f"게시글 내용: {content}")
    print(f"욕설 포함 여부: {'O' if is_valid else 'X'}")


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.title, args.content)
