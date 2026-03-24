from agent import create_research_agent, run_agent


def main():

    print("=" * 60)
    print("🔍 Research Agent")
    print("=" * 60)
    print("Я — дослідницький агент. Задай мені питання, і я знайду")
    print("інформацію в інтернеті та створю структурований звіт.")
    print()
    print("Команди:")
    print("  'exit' або 'quit' — вийти")
    print("  'new' — почати нову сесію (очистити контекст)")
    print("=" * 60)
    print()


    try:
        agent = create_research_agent()
        print("✅ Агент готовий до роботи!\n")
    except ValueError as e:
        print(f"❌ Помилка: {e}")
        return
    except Exception as e:
        print(f"❌ Не вдалося створити агента: {e}")
        return

    # ID сесії для збереження контексту розмови
    session_id = "session_1"
    session_counter = 1


    while True:
        try:
            # Отримуємо запит від користувача
            user_input = input("📝 Ти: ").strip()

            # Перевіряємо спеціальні команди
            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "вихід", "вийти"]:
                print("\n👋 До побачення!")
                break

            if user_input.lower() in ["new", "нова", "очистити"]:
                session_counter += 1
                session_id = f"session_{session_counter}"
                print("🔄 Розпочато нову сесію. Контекст очищено.\n")
                continue


            print("\n🤖 Агент думає...\n")

            response = run_agent(agent, user_input, session_id)

            print("🤖 Агент:")
            print("-" * 40)
            print(response)
            print("-" * 40)
            print()

        except KeyboardInterrupt:
            print("\n\n👋 До побачення!")
            break
        except Exception as e:
            print(f"\n❌ Помилка: {e}\n")


if __name__ == "__main__":
    main()