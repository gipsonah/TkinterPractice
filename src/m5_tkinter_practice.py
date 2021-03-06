"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Alex Gipson.
"""  # DO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DO: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()

    # ------------------------------------------------------------------
    # DO: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # ------------------------------------------------------------------
    # DO: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    say_hello_button = ttk.Button(frame1, text='Say Hello')
    say_hello_button.grid()

    # ------------------------------------------------------------------
    # DO: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    say_hello_button['command'] = (lambda: print_hello())

    # ------------------------------------------------------------------
    # DO: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    hello_goodbye_button = ttk.Button(frame1, text='test for ok')
    hello_goodbye_button['command'] = (lambda: test_for_ok(my_entry_box))
    hello_goodbye_button.grid()

    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    todo_button = ttk.Button(frame1, text='To Do 7')
    todo_button.grid()
    entry_box = ttk.Entry(frame1)
    entry_box.grid()
    todo_button['command'] = (lambda: To_do_7(entry_box, my_entry_box))
    todo_button.grid()

    # ------------------------------------------------------------------
    # DO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.mainloop()

def print_hello():
    print('Hello')

def test_for_ok(entry_box):
    contents = entry_box.get()
    if contents == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def To_do_7(entry_box, my_entry_box):
    a = my_entry_box.get()
    s = entry_box.get()
    n = int(s)
    for k in range(n):
        print(str(a))


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
