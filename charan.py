def combine(data):
    
    tools, expertise, connect_with_me = data
    
    # Print tools
    print("Tools:")
    for tool in tools:
        print("-", tool)
    
    # Print expertise
    print("\nExpertise:")
    for skill in expertise:
        print("-", skill)
    
    # Print connection information
    print("\nConnect with me:")
    for platform, link in connect_with_me.items():
        print(f"- {platform}: {link}")
