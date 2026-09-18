class Solution:

    def isValid(self, s: str) -> bool:

        open_b = "([{"       # round, square, curly
        close_b = ")]}"      # round, square, curly
        st = []

        for i in s:

            # Open brackets go into the stack
            if i in open_b:
                st.append(i)

            else:    # When a closed bracket is encountered

                # If stack is empty, sequence is invalid
                if not st:
                    return False

                # Check if stack top is corresponding open bracket
                if ((i == ")" and st[-1] == "(") or
                    (i == "]" and st[-1] == "[") or
                    (i == "}" and st[-1] == "{")):

                    st.pop()

                else:
                    return False

        # Valid only if stack is empty
        return not st