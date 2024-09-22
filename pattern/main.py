from findpattern  import findPattern


if __name__ == "__main__":
    result  = []
    pattern = "developer"
    frames = [
        "aprghadeveloperadedepeperdeveloper",
        "nonongreedeveeloper",
        "totododdevelopper",
        "appaapapapdevelloper",
        "webewewebdevevelopeeeradfdefdeveloper",
    ]

    for f in frames:
        result.append(findPattern(pattern, f))
    
    print("Result: ", result)
    