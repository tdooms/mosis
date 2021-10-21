#
# scanner.py
#
# Based on code for COMP 304B Assignment 3
# Updated to Python 3 in 2021
#
import re

# trace FSA dynamics (True | False)
__trace__ = False


class LineStream:
    """
    A stream of lines helper class.
    """

    def __init__(self, string):
        self.string = string.split("\n")
        self.last_ptr = -1
        self.cur_ptr = -1

    def __repr__(self):
        return self.string

    def __str__(self):
        return self.string

    def peek(self):
        if self.cur_ptr + 1 < len(self.string):
            return self.string[self.cur_ptr + 1]
        return None

    def consume(self):
        self.cur_ptr += 1

    def commit(self):
        self.last_ptr = self.cur_ptr

    def rollback(self):
        self.cur_ptr = self.last_ptr


class CharacterStream:
    """
    A stream of characters helper class.
    """

    def __init__(self, string):
        self.string = string
        self.last_ptr = -1
        self.cur_ptr = -1

    def __repr__(self):
        return self.string

    def __str__(self):
        return self.string

    def peek(self):
        if self.cur_ptr + 1 < len(self.string):
            return self.string[self.cur_ptr + 1]
        return None

    def consume(self):
        self.cur_ptr += 1

    def commit(self):
        self.last_ptr = self.cur_ptr

    def rollback(self):
        self.cur_ptr = self.last_ptr


class Scanner:
    """
    A simple Finite State Automaton simulator.
    Used for scanning an input stream.
    """

    def __init__(self, stream):
        self.set_stream(stream)
        self.current_state = None
        self.accepting_states = []

    def set_stream(self, stream):
        self.stream = stream

    def scan(self):
        self.current_state = self.transition(self.current_state, None)

        if __trace__:
            print("\ndefault transition --> " + self.current_state)

        while True:
            # look ahead at the next character in the input stream
            next_char = self.stream.peek()

            # stop if this is the end of the input stream
            if next_char is None: break

            if __trace__:
                if self.current_state is not None:
                    print("transition", self.current_state, "-|", next_char,
                          end=' ')

            # perform transition and its action to the appropriate new state
            next_state = self.transition(self.current_state, next_char)

            if __trace__:
                if next_state is None:
                    print("")
                else:
                    print("|->", next_state)

            # stop if a transition was not possible
            if next_state is None:
                break
            else:
                self.current_state = next_state
                # perform the new state's entry action (if any)
                self.entry(self.current_state, next_char)

            # now, actually consume the next character in the input stream
            next_char = self.stream.consume()

        if __trace__:
            print("")

        # now check whether to accept consumed characters
        success = self.current_state in self.accepting_states
        if success:
            self.stream.commit()
        else:
            self.stream.rollback()
        return success


class TrolleyIsOnJunctionScanner(Scanner):
    def __init__(self, stream):
        # superclass constructor
        super().__init__(stream)

        # define accepting states
        self.accepting_states = ["init"]

    def entry(self, state, input):
        pass

    def transition(self, state, input):
        """
        Encodes transitions and actions
        :param state: The state in which we are currently
        :param input: The input we get
        :return: The state in which we are next given the input-parameters
        """
        if input is None:
            return "init"

        if state is None:
            return None
        elif state == "init":
            if input == "E 3":
                return "locked"
            else:
                return "init"
        elif state == "eof":
            return "eof"
        elif state == "locked":
            if input == "X 3":
                return "init"
            elif re.match("(R [12])|(E [12])", input):
                return "locked"


class TrolleyPriorityScanner(Scanner):
    def __init__(self, stream):
        # superclass constructor
        super().__init__(stream)

        # define accepting states
        self.accepting_states = ["loop"]

    def entry(self, state, input):
        pass

    def transition(self, state, input):
        """
        Encodes transitions and actions
        :param state: The state in which we are currently
        :param input: The input we get
        :return: The state in which we are next given the input-parameters
        """

        if input is None:
            return "init"

        if state is None:
            return "init"

        elif state == "init":
            if input == "E 1":
                return "q12"
            elif input == "E 2":
                return "q22"
            elif input is None:
                return "end"
            else:
                return "init"

        elif state == "q12":
            if input == "E 2": return "q13"
            if input == "G 1":
                return "init"
            else:
                return "q12"

        elif state == "q13":
            if input == "G 2":
                return "loop"
            elif input == "G 1":
                return "init"
            else:
                return "q13"

        elif state == "q22":
            if input == "E 1":
                return "q23"
            elif input == "G 2":
                return "init"
            else:
                return "q22"

        elif state == "q23":
            if input == "G 1":
                return "loop"
            elif input == "G 2":
                return "init"
            else:
                return "q23"

        elif state == "loop":
            return "loop"


if __name__ == "__main__":
    for i in range(1, 7):
        f = open(f"input/trace{i}.txt", "r")
        stream = LineStream(f.read())
        scanner = TrolleyIsOnJunctionScanner(stream)
        success = scanner.scan()
        f2 = open(f"input/trace{i}.txt", "r")
        stream2 = LineStream(f2.read())
        scanner2 = TrolleyPriorityScanner(stream2)
        success2 = scanner2.scan()
        f = open(f"input/trace{i}.txt", "r")
        file = f.read()

        # print(re.match("(. .\n)*(((E 1\n)([^G] .\n)*(E 2\n)([^G] .\n)*(G 2\n))|((E 2\n)([^G] .\n)*(E 1\n)([^G] .\n)*(G 1\n)))(. .\n)*", file))
        print("\nUse case: trolley is on junction")
        if success:
            print(f"Stream {i} has been accepted.")
        else:
            print(f"Stream {i} not accepted.")

        print("\nUse case: trolley priority")
        if not success2:
            print(f"Stream {i} has been accepted.")
        else:
            print(f"Stream {i} not accepted.")
