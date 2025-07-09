import time
import random

# قائمة الألغاز (سأضع أمثلة فقط، ويمكنك إكمالها حتى 60)
puzzles = [
    {"question": "ما هو الشيء الذي يمشي بلا أرجل؟", "answer": "الظل"},
    {"question": "ما هو الشيء الذي ينبض بلا قلب؟", "answer": "الساعة"},
    {"question": "شيء تراه ولا يراك؟", "answer": "المرآة"},
    {"question": "ما هو أهون موجود وأعز مفقود؟", "answer": "الماء"},
    {"question": "له أوراق وما هو بنبات، له جلد وما هو بحيوان، يعلم وما هو بإنسان؟", "answer": "الكتاب"},
    # أضف المزيد هنا حتى 60
]

# يمكنك خلط ترتيب الألغاز إن أردت
random.shuffle(puzzles)

def show_welcome():
    print("="*50)
    print("🎉 أهلاً بك في لعبة الألغاز العربية 🎉")
    print("="*50)
    print("\nفي هذه اللعبة، ستواجه 60 لغزًا. كل إجابة صحيحة تمنحك 10 نقاط.")
    input("\nاضغط Enter للبدء...")

def play_game():
    score = 0
    total_puzzles = len(puzzles)

    for i, puzzle in enumerate(puzzles, start=1):
        print(f"\n🔹 اللغز رقم {i}/{total_puzzles}:")
        print(puzzle["question"])
        answer = input("إجابتك: ").strip()

        if answer == puzzle["answer"]:
            print("✅ إجابة صحيحة!")
            score += 10
        else:
            print(f"❌ خطأ. الإجابة الصحيحة هي: {puzzle['answer']}")

        print(f"النقاط الحالية: {score}")
        time.sleep(1)

    show_result(score, total_puzzles)

def show_result(score, total_puzzles):
    print("\n🎊 لقد أنهيت اللعبة! 🎊")
    print("="*40)
    print(f"مجموع نقاطك: {score} من {total_puzzles * 10}")
    if score == total_puzzles * 10:
        print("🔥 ممتاز! لقد أجبت على كل الألغاز بشكل صحيح!")
    elif score >= total_puzzles * 7:
        print("👏 جيد جدًا!")
    else:
        print("💡 حاول مرة أخرى لتحسين نتيجتك!")
    print("="*40)

# تشغيل اللعبة
show_welcome()
play_game()
