from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [python, ruby, visual_basic]
dynamically_typed_languages = [language.language for language in languages if language.is_dynamic()]
print("The dynamically typed languages are:")
for dynamically_typed_language in dynamically_typed_languages:
    print(dynamically_typed_language)
