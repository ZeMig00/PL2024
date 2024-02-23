import re, sys

class parser:

    def rule_header(self, str):
        for m in re.findall(r'(?:^|\n)((#+)\s(.*))', str):
            str = str.replace(m[0], f"<h{len(m[1])}>{m[2]}</h{len(m[1])}>")
        return str
    
    def rule_bold(self, str):
        for m in re.findall(r'(\*\*(.*)\*\*)', str):
            str = str.replace(m[0], f"<b>{m[1]}</b>")
        return str
    
    def rule_italico(self, str):
        for m in re.findall(r'(\*(.*)\*)', str):
            str = str.replace(m[0], f"<i>{m[1]}</i>")
        return str

    def rule_lista(self, str):
        out = ""
        block_started = False
        for line in str.split('\n'):
            m = re.findall(r'(\d+)\.(.*)', line)

            if len(m) == 1 and block_started == False:
                out += "<ol>\n"
                block_started = True
            
            if len(m) == 1:
                out += "<li>" + m[0][1] + "</li>\n"
            elif block_started == True:
                out += "</ol>\n"
                block_started = False

            if block_started == False:
                out += line + "\n"
        
        if block_started == True:
            out += "</ol>"
        return out
    
    def rule_link(self, str):
        for m in re.findall(r'(\[(.*)\]\((.*)\))', str):
            str = str.replace(m[0], f'<a href="{m[2]}">{m[1]}</a>')
        return str
    
    def rule_image(self, str):
        for m in re.findall(r'(\!\[(.*)\]\((.*)\))', str):
            str = str.replace(m[0], f'<img src="{m[2]}" alt="{m[1]}"/>')
        return str
    
    def run(self, str):
        return self.rule_header(
                self.rule_italico(
                    self.rule_bold(
                        self.rule_lista(
                            self.rule_link(
                                self.rule_image(
                                    str
                                )
                            )
                        )
                    )
                )
            )
    

def main():
    print("<html>")
    print(parser().run(sys.stdin.read()))
    print("</html>")
    return 0

if __name__ == "__main__":
    exit(main())