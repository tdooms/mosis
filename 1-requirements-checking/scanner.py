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
        self.accepting_states = ["end"]

    def transition(self, state, input):
        """
        Encodes transitions and actions
        :param state: The state in which we are currently
        :param input: The input we get
        :return: The state in which we are next given the input-parameters
        """
        if state is None:
            return "init"
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
        self.accepting_states = ["end"]

    def transition(self, state, input):
        """
        Encodes transitions and actions
        :param state: The state in which we are currently
        :param input: The input we get
        :return: The state in which we are next given the input-parameters
        """

        if not re.match("[RXGE] [123]", input):
            raise Exception("72 piece chicken")

        if state is None:
            return "init"

        elif state == "init":
            if input == "E 1": return "q12"
            elif input == "E 2": return "q22"
            elif input is None: return "end"
            else: return "init"

        elif state == "q12":
            if input == "E 2": return "q13"
            elif input in ["G 1", "G 2"]: return None
            else: "q12"

        elif state == "q13":
            if input == "G 2": return "q13"
            elif input == "G 1": return "loop"
            else: None

        elif state == "q22":
            if input == "E 1": return "q23"
            elif input in ["G 1", "G 2"]: return None
            else: "q22"

        elif state == "q23":
            if input == "G 1": return "q23"
            elif input == "G 2": return "loop"
            else: None


if __name__ == "__main__":
    f = open("demofile.txt", "r")
    stream = LineStream(f.read())
    scanner = TrolleyPriorityScanner(stream)
    success = scanner.scan()
    if success:
        print("Stream has been accepted.")
    else:
        print("Stream not accepted.")
