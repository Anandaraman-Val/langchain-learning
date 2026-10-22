import os

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("Hello from langchain-learning!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
