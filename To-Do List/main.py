def Choose():
    choice = input("""
Please choose an option:
Exit: 0 or 'exit'
Show To-Dos: 1 or 'show'
Add To-Do: 2 or 'add'
Set completion to a To-Do: 3 or 'set'
Delete To-Do: 4 or 'delete'
Save To-Do list: 5 or 'save'
>"""
    ).lower()
    match choice:
        case '0' | 'exit':
            print("\nThank you for using my app. :)")
            quit()
        case '1' | 'show':
            return 1
        case '2' | 'add':
            return 2
        case '3' | 'set':
            return 3
        case '4' | 'delete':
            return 4
        case '5' | 'save':
            return 5
        case _:
            print("Invalind input, returning default(1)")
            return 1

def Add(to_do : list[str]) -> list[str]:
    element = input("\nPlease add an element to the To-Do list:\n>")
    to_do.append(element)
    return to_do

def Show(to_do : list[str], completed : list[str]) -> None:
    if not to_do:
        print("\nNothing to do. :)")
        return
    for i in to_do:
        print(f"\n[✅] {i}" if i in completed else f"\n[❌] {i}")

def Set(to_do : list[str], completed : list[str]) -> list[str]:
    max_idx = 0
    if to_do == completed:
        print("\nNothing to complete. :)")
        return completed
    print("\nPlease select a task, that you would like to mark as completed:")
    for idx,to in enumerate(to_do):
        if to not in completed:
            print(f"\n[{idx}] {to}")
        max_idx = idx
    choice = int(input(">"))
    completed.append(to_do[choice]) if choice <= max_idx and choice > -1 else print("Invalid input")
    return completed

def Delete(to_do : list[str], completed : list[str]) -> tuple[list[str],list[str]]:
    max_idx = 0
    if not to_do:
        print("\nNothing to delete. :)")
        return to_do,completed
    print("\nPlease select a task, that you would like to Delete!")
    for idx,task in enumerate(to_do):
        print(f"[{idx}] {task}")
        max_idx = idx
    choice = int(input('>'))
    if to_do[choice] in completed:
        completed.remove(to_do[choice])
    to_do.remove(to_do[choice]) if choice <= max_idx and choice > -1 else print("Invalid input")
    return to_do,completed

def Save(to_do : list[str],completed : list[str]) -> None:
    if not to_do:
        print("\nNothing to save. :)")
        return
    import os
    import pathlib
    file_name = input("\nPlease give a name to the file:\n>")
    current_path = pathlib.Path(__file__).parent.resolve()
    if os.path.exists(f"{current_path}\{file_name}.txt"):
        with open(f"{current_path}\{file_name}.txt","a") as f:
            for idx,task in enumerate(to_do):
                if task not in completed:
                    f.write(f"[X] {task}\n")
    else: 
        with open(f"{current_path}\{file_name}.txt","x") as f:
            for idx,task in enumerate(to_do):
                if task not in completed:
                    f.write(f"[X] {task}\n")

if __name__ == "__main__":
    to_do = []
    completed = []
    while 1:
        match Choose():
            case 1:
                Show(to_do,completed)
            case 2:
                Add(to_do)
            case 3:
                Set(to_do,completed)
            case 4:
                Delete(to_do,completed)
            case 5:
                Save(to_do,completed)
            case _:
                print("\n❕❕❕Please select from the list❕❕❕")