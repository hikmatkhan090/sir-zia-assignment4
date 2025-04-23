def generate_story(name, language, mentor):
    story = f"""
    🌟 An Inspiring Tech Journey: The Extraordinary Story of {name} 🌟

    In a vibrant city, lived a young boy named {name}, whose curiosity knew no bounds. 
    While most children his age were captivated by games and entertainment, {name} found himself drawn to the fascinating world of technology, eager to explore its endless possibilities.

    One day, while navigating the vast realm of the internet, {name} discovered something that instantly caught his attention—{language}. 
    It was love at first sight, and he knew right then that he was destined to master {language}.

    Fueled by an unwavering determination, {name} sought the best platform to nurture his newfound passion. 
    That’s when he heard about the renowned Governor House program, known for equipping students with cutting-edge skills in technology. 
    Without a second thought, {name} applied, and he was overjoyed when he was selected to join the program!

    However, mastering {language} was not a walk in the park. {name} faced many sleepless nights, moments of self-doubt, and frustrations from countless bugs in his code. 
    There were times when the road ahead seemed impossible, but {name} refused to let go of his dreams. 
    He knew that true success required resilience, patience, and hard work.

    It was during these challenging times that {name} met his mentor, {mentor}, a seasoned expert in {language} with years of experience. 
    {mentor} became more than just a teacher—he was a guiding light, providing wisdom and encouragement when it was needed the most.

    With {mentor}’s guidance, {name} learned not just how to write code, but how to approach problems with a creative and analytical mindset. 
    {mentor} taught him that programming was not just about syntax—it was about solving real-world problems with ingenuity, passion, and a little bit of magic.

    Slowly, but surely, {name} began to build projects, fix bugs, and develop a deep confidence in his abilities. 
    His perseverance paid off when he completed his first major project—a groundbreaking app created using {language}. 
    It was a moment of immense pride, and when the project was presented to industry experts, {name} felt the sense of accomplishment he had long worked for.

    From a curious beginner to a capable programmer, {name}’s journey was a true testament to the power of passion, persistence, and the right guidance. 
    His story serves as a beacon of inspiration for anyone who believes in the power of learning and growth.

    🚀 And so, {name} continues his journey, ever hungry for knowledge, pushing boundaries, and proving that with the right mindset, anything is possible!

    🌱 The story of {name} reminds us that the path to success is not always easy, but it is always worth it when we put our heart and soul into what we love.

    The End 🎉
    """
    return story


def main():
    print("👨‍💻 Welcome to the Madlibs - Inspirational Story Generator!\n")

    name = input("Enter the boy's name: ")
    language = input("Enter a programming language (e.g: Python, Next.js, TypeScript, HTML): ")
    mentor = input("Enter the mentor's name: ")

    print("\n✨ Here is your personalized story:\n")
    print(generate_story(name, language, mentor))


if __name__ == "__main__":
    main()
