from argparse import ArgumentParser
import terminology

def test():
    print("Testing...")
    term1 = terminology.Term("Virtual Private Network")
    term2 = terminology.Term("Domain Name System", ["network layer", "protocol"])

    print(term1)
    print(term2)

    #print("Is 'protocol' a keyword for term1?", term1.matches("protocol"), "(should be False)")
    #print("Is 'protocol' a keyword for term2?", term2.matches("protocol"), "(should be True)")
    #print("Is 'layer' a keyword for term2?", term2.matches("layer"), "(should be True)")

    '''
    glossary = terminology.Glossary()
    glossary.add(term1)
    glossary.add(term2)
    print("The terms in the glossary in alphabetical order are:", [str(term) for term in glossary.terms])
    print("What is the term for the acronym VPN?", glossary.lookup_by_acronym("VPN"))
    print("What is the term for the acronym TCP?", glossary.lookup_by_acronym("TCP"))
    print("What are the terms for the keyword 'protocol'?", [str(term) for term in glossary.lookup_by_keyword("protocol")])
    '''

def lookup_acronym(glossary, acronym):
    print("Looking up terms by acronym will fail until the Glossary class is implemented")
    term = glossary.lookup_by_acronym(acronym)
    if (term):
        print(term)
        for term in term.keywords:
            print(f"- {term}")
    else:
        print(f"No term with acronym {acronym}")

def lookup_keyword(glossary, keyword):
    print("Looking up terms by keyword is not currently supported")

def display_terms(glossary):
    print("Run the program with the -h command-line argument to see the help output:")
    print("  python3 reference.py -h")

def main():
    # Parse arguments
    parser = ArgumentParser(description='Networking words')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--test', dest='test', action='store_true',
            help='Enable test mode') 
    group.add_argument('-a', '--acronym', dest='acronym', action='store',
            type=str, help='Acronym for term to lookup', default=None) 
    group.add_argument('-k', '--keyword', dest='keyword', action='store',
            type=str, help='Keyword to lookup', default=None)
    settings = parser.parse_args()

    if (settings.test):
        test()
    else:
        glossary = None
        #glossary = terminology.Glossary.load()
        if (settings.acronym):
            lookup_acronym(glossary, settings.acronym.upper())
        elif (settings.keyword):
            lookup_keyword(glossary, settings.keyword.lower())
        else:
            display_terms(glossary) 

if __name__ == '__main__':
    main()