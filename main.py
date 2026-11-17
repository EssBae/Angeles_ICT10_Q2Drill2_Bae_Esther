from pyscript import document
output_div = document.querySelector("#output")
message = document.querySelector("#message")

Grade_7 = {"Mateo Reyes", "Chloe Tan"}
Grade_8 = {"Isabella Cruz", "Noah Santos"}
Grade_9 = {"Lucas Garcia", "Sofia Mendoza"}
Grade_10 = {"Olivia Ramos", "Gabriel Navarro"}
new_members = set()

def show_members():
    member_list = Grade_7 | Grade_8 | Grade_9 | Grade_10 | new_members
    print(member_list)
    output_div.innerText = ", ".join(sorted(member_list))

def add_member(event):
    first = document.querySelector("#first").value
    last = document.querySelector("#last").value
    new_members.add(f"{first} {last}")
    message.innerText = f"{first} {last} was successfully added!"
    show_members()

show_members()








