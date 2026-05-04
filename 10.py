def chatbot():
    print("Chatbot: Hello! Welocme to our stoe. Type 'exit' to quit. ")

    while True:
        user_Input = input("User: ").lower()

        if user_Input == "exit" :
            print("Chatbot: Thank you! Have a nice day.")
            break

        elif "hello" in user_Input or "hi" in user_Input:
            print("Chatbot: Hello! How can I help you?")
            continue

        elif "price" in user_Input:
            print("Chatbot: Prices vary depending on the item. Please specify the item or check the product description for price.")
            continue

        elif "order" in user_Input:
            print("Chatbot: Please check the 'My Orders' section in Profile for order details")
            continue

        elif "delivery" in user_Input:
            print("Chatbot: Product delivery usually takes 5-7 working days.")
            continue

        elif "contact" in user_Input:
            print("Chatbot: You can contact us at support@company.com")
            continue

        else:
            print("Chatbot: Sorry, I don't understand that. Please rephrase it")



chatbot()
