def compileJava(inputText, fileName):
    if inputText is not None and inputText!='':
        compile = subprocess.Popen(["javac", fileName], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        output = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=inputText.encode())
    else:
        compile = subprocess.Popen(["javac", fileName], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        output = subprocess.Popen(["java", "Main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return output

def compileCPP(inputText, fileName):
    if inputText is not None and inputText!='':
        compile = subprocess.Popen(["g++", fileName], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        output = subprocess.Popen(["./a.out"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=inputText.encode())
    else:
        compile = subprocess.Popen(["g++", fileName], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        output = subprocess.Popen(["./a.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return output

def compilePython(version, inputText, fileName):
    if inputText is not None and inputText!='':
        output = subprocess.Popen([version, fileName], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=inputText.encode())
    else:
        output = subprocess.Popen([version, fileName], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return output