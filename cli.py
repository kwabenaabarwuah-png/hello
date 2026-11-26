from app import add_note, list_notes

def main():
    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("> ").strip()
        if choice == "1":
            text = input("Note: ").strip()
            if text:
                add_note(text)
                print("Saved.")
        elif choice == "2":
            notes = list_notes()
            if not notes:
                print("No notes yet.")
            for note_id, text in notes:
                print(f"{note_id}: {text}")
        elif choice == "3":
            break
        else:
            print("Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
