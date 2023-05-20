from langdetect import detect, detect_langs
from termcolor import cprint

def language_detection(text, method = "single"):
  if(method.lower() != "single"):
    result = detect_langs(text)
    for item in result:
      cprint("Detected Language: " + item.lang + " Probability: " + str(item.prob), "green", attrs=["bold"])
  else:
    result = detect(text)
    cprint("Detected Language: " + result, "green", attrs=["bold"])
    return 1

if __name__ == "__main__":
    text = input("Enter text to detect: ")
    cprint("""=== LEGEND ===\nSingle method outputs only the language code with the highest probability.\nMultiple method outputs all the language codes with their probabilities.  \n==============\n""", "green",  attrs=["bold"] )
    method = input("Enter method (single or multiple): ")

    if method.lower() == "single":
        language_detection(text)
    elif method.lower() == "multiple":
        language_detection(text, method)
    else:
        cprint("Invalid method.", "red", attrs=["bold"])