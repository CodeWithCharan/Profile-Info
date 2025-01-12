def combine(data):
    
    languages, tech, data_analysis, connect_with_me = data
    
    # Print languages
    print("Languages:")
    for language in languages:
        print("-", language)

    # Print technologies
    print("\nTechnologies:")
    for t in tech:
        print("-", t)
    
    # Print data analysis
    print("\nData Analysis:")
    for da in data_analysis:
        print("-", da)
    
    # Print connection information
    print("\nConnect with me:")
    for platform, link in connect_with_me.items():
        print(f"- {platform}: {link}")
