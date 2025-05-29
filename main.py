from database import setup_database
import blog_operations

def print_menu():
    print("\nBLOG PLATFORM MENU")
    print("1. Add Post")
    print("2. View All Posts")
    print("3. Update Post")
    print("4. Delete Post")
    print("5. Exit")

def main():
    setup_database()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter title: ")
            content = input("Enter content: ")
            category = input("Enter category: ")
            blog_operations.add_post(title, content, category)

        elif choice == '2':
            posts = blog_operations.view_posts()
            for post in posts:
                print(f"\nID: {post[0]}")
                print(f"Title: {post[1]}")
                print(f"Content: {post[2]}")
                print(f"Category: {post[3]}")
                print(f"Posted on: {post[4]}")

        elif choice == '3':
            post_id = int(input("Enter post ID to update: "))
            title = input("New title: ")
            content = input("New content: ")
            category = input("New category: ")
            blog_operations.update_post(post_id, title, content, category)

        elif choice == '4':
            post_id = int(input("Enter post ID to delete: "))
            blog_operations.delete_post(post_id)

        elif choice == '5':
            print("Exiting Blog Platform.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":  #for future if i export it
    main()
