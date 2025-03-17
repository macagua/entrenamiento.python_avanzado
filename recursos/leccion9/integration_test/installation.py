"""Social networks components integration"""

import instagram
import whatsapp

def sent_message(fun):
    """Sent message for every social networks components

    Args:
        fun (funt): The social network greeting function

    Returns:
        str: The social network greeting
    """
    return fun

def instagram_integration():
    """Sent message to Instagram component"""
    return sent_message(instagram.greetings())

def whatsapp_integration():
    """Sent message to WhatsApp component"""
    return sent_message(whatsapp.greetings())

if __name__ == '__main__':
    print(f"📜 The Instagram message is: '{instagram_integration()}'.")
    print(f"📜 The Whatapp message is: '{whatsapp_integration()}'.")
