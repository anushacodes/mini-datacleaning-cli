import argparse
from dataz.commands.view import view
from dataz.commands.summarize import summarize



def main():

    parser = argparse.ArgumentParser(description="data preparation CLI tool")

    parser.add_argument("--i", "--input", required = True, dest = "i", help="path to your input dataset")
    parser.add_argument("--o", "--output", dest = 'output', help="path to your output dataset")

    parser.add_argument("--v", "--view", dest = "v", action="store_true", help="preview the dataset")
    parser.add_argument("--s", "--summarize", dest = "s", action="store_true", help="summarize the dataset")

    args = parser.parse_args()

    if args.v:
        view(args)

    elif args.s:
        summarize(args)

    else:
        parser.print_help()



if __name__ == "__main__":
    main()








