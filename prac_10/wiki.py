import wikipedia


def main():
    query = input("Search: ")
    while query != "":
        try:
            page = wikipedia.page(query, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as e:
            print("Ambiguous. Did you mean one of the following?")
            counter = 1
            for option in e.options:
                if counter == len(e.options) or "(disambiguation)" in option.split(" "):
                    break
                print(f"{counter}. {option}")
                counter += 1
            try:
                choice = int(input("Enter number: "))
                page = wikipedia.page(e.options[choice - 1])
                print_page(page)
            except TypeError:
                print("Invalid number")
            except IndexError:
                print("Invalid number")
        else:
            print_page(page)
        query = input("Search: ")


def print_page(page):
    print(f"\nTitle:   {page.title}\n\n"
          f"Summary: {page.summary}\n\n"
          f"URL:     {page.url}\n")


main()
