import pandas as pd
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")


def generate_example_sentence(word, model="gpt-3.5-turbo"):
    instruction = "you are professional english teacher."
    prompt = f"generate two example sentence with {word}"

    messages = [
        {"role": "system", "content": instruction},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


def try_five_times(func):
    def wrapper(**kwargs):
        error_count = 0
        while error_count < 5:
            try:
                print(f"trial {error_count + 1}")
                func(**kwargs)
                print("success!")
                break
            except Exception as e:
                error_count += 1
                print(e)

    return wrapper


@try_five_times
def make_complete_vocab_list(input_path=r"mycsv.csv",
                             output_path=r"mycsv.csv"):
    # CSV 파일 불러오기
    df = pd.read_csv(input_path, encoding='utf-8-sig')

    # 예문이 비어 있는 행을 찾아 채우기
    for index, row in df.iterrows():
        if pd.isna(row['예문']):
            word = row['단어']
            generated_example = generate_example_sentence(word)
            df.at[index, '예문'] = str(generated_example)

            # 변경된 DataFrame을 즉시 CSV 파일로 저장
            df.to_csv(output_path, index=False, encoding='utf-8-sig')
            print(f"예문 생성 for {word}: \n{generated_example}")

    df['예문'] = df['예문'].astype(str)


if __name__ == "__main__":
    make_complete_vocab_list()
