#Define Task Class:
#Create a Task class with attributes such as task title, description, due date, and status.
class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return (
            f'Vazifa: {self.title}\n'
            f'Tavsif: {self.description}\n'
            f'Vaqti: {self.due_date}\n'
            f'Statusi: {self.status}'
        )

# Example usage
task1 = Task('Hisobot topshirish', 'Oylik hisobot', '2025-06-01', 'Kutilmoqda')
print(task1)


#Define ToDoList Class:
#Create a ToDoList class that manages a list of tasks.
#Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
class Task:
    def __init__(self, title, description, due_date, status='pending'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = 'complete'

    def __str__(self):
        return f"{self.title} | {self.description} | {self.due_date} | {self.status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()

    def list_all_tasks(self):
        for task in self.tasks:
            print(task)

    def display_incomplete_tasks(self):
        for task in self.tasks:
            if task.status != 'complete':
                print(task)


# Create tasks
t1 = Task('Hisobot', 'Topshirish', '2025-09-09')
t2 = Task('Email', 'Yuborish', '2025-10-10')

# Create ToDoList
todo = ToDoList()
todo.add_task(t1)
todo.add_task(t2)

# Print all tasks
print("Barcha:")
todo.list_all_tasks()

# Mark task as complete
todo.mark_task_complete('Email')

# Print incomplete tasks
print("Bajarilmagan:")
todo.display_incomplete_tasks()

#Define Post Class:
#Create a Post class with attributes like title, content, and author.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content 
        self.author = author

    def __str__(self):
        return (
            f'Sarlavha: {self.title}\n'
            f'Matn: {self.content}\n'
            f'Muallif: {self.author}'
        )

# Create and print post
post1 = Post('Python darsi', 'Bugun klassik mavzular', 'Sherlok Xomis')
print(post1)

#Define Blog Class:
#Create a Blog class that manages a list of posts.
#Include methods to add a post, list all posts, and display posts by a specific author.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content 
        self.author = author

    def __str__(self):
        return f"Sarlavha: {self.title}\nMuallif: {self.author}\nMatn: {self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("Hozircha hech qanday post mavjud emas.")
        else:
            for post in self.posts:
                print(post)
                print("-" * 40)

    def show_post_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)
                print("-" * 40)
                found = True
        if not found:
            print(f"{author} nomli muallif tomonidan yozilgan post topilmadi.")


def main():
    blog = Blog()

    # Postlar yaratish
    p1 = Post("Python darsi", "Bugun klasslar mavzusini o‘rganamiz.", "Ali")
    p2 = Post("Math asoslari", "Algebra va geometriya haqida.", "Vali")
    p3 = Post("OOP dasturlash", "Klasslar va obyektlar haqida.", "Ali")

    # Blogga qo‘shish
    blog.add_post(p1)
    blog.add_post(p2)
    blog.add_post(p3)

    print("Barcha postlar:")
    blog.list_all_posts()

    print("\nAli yozgan postlar:")
    blog.show_post_by_author('ali')


if __name__ == '__main__':
    main()

#Define Account Class:
#Create an Account class with attributes like account number, account holder name, and balance.
class Account:
    def __init__(self,account_number,account_holder_name,acccount_balance=0.0):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.acccount_balance=acccount_balance
    def __str__(self):
        return f'account[{self.account_number}]-{self.account_holder_name},Balance:{self.acccount_balance}'
acc1 = Account("12345678", "Ali Valiyev", 2500.0)
print(acc1)

#Define Bank Class:
#Create a Bank class that manages a list of accounts.
#Include methods to add an account, check balance, deposit money, and withdraw money.
class Account:
    def __init__(self, account_number, account_holder_name, account_balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            return account.account_balance
        else:
            return 'Account not found'

    def withdraw_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if account.withdraw(amount):
                return f'Withdrew ${amount} from account {account_number}'
            else:
                return "Insufficient balance or invalid amount"
        else:
            return "Account not found"

    def deposit_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if account.deposit(amount):
                return f'Deposited ${amount} to account {account_number}'
            else:
                return "Invalid deposit amount"
        else:
            return "Account not found"

my_bank = Bank()
acc1 = Account("123", "Alice", 1000)
acc2 = Account("456", "Bob", 500)

# Add accounts to the bank
my_bank.add_account(acc1)
my_bank.add_account(acc2)

# Deposit money
print(my_bank.deposit_money("123", 200))  # Deposited $200 to account 123

# Withdraw money
print(my_bank.withdraw_money("123", 300))  # Withdrew $300 from account 123

# Check balance
print(my_bank.check_balance("123"))  # 900.0
