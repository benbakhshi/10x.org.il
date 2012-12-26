"""
Cash Register (cash_register.py)
================================

Problem
-------
Build an interactive cash register!

When started the cashier is presented by a welcome message:

Welcome to 10x cash register!
Please enter the amount of funds currently deposited in the register:

The register remembers the number entered by the cashier.
(A blank line is treated as a 0).

The following help text is now displayed:

Enter a positive number to add to the bill
Enter a negtive number to deduct from the bill
Enter x to cancel the current bill.
Enter 0 to checkout bill and accept payment.
Enter 00 to show the cash register status.
Enter 000 to end the day and exit.

The cash register is now ready to accept the first bill.
It shows the following prompt:

[Bill #1] Subtotal: $0

The cashier can enter one of the optoins described in the help text above.
The prompt is updated as needed, for example:

[Bill #1] Subtotal: $0
35
[Bill #1] Subtotal: $35
20
[Bill #1] Subtotal: $55
100
[Bill #1] Subtotal: $155
-20
[Bill #1] Subtotal: $135
0

(An empty line is ignored, and the prompt is displayed again)

When the cashier checkouts, the bill subtotal is added to the
cash register total and it is displayed as following
(We assume the initial amount in the regsiter was 200):

Bill #1 Payment accepted: $135
Grand Total: $335

And the cashier is ready to accept the next bill:

[Bill #2] Subtotal: $0

(Note: If the cashier tries to checkout when the subtotal is $0,
The checkout attempt is ignored, and the prompt is displayed again)

If the cashier wants to cancel the current bill, he enters x:

[Bill #32] Subtotal: $106
x

The following is displayed:

Bill #32 canceled.
Grand Total: $765
[Bill #33] Subtotal: $0

If the cashier enters 00, the grand total is printed out,
and the prompt is displayed again:

[Bill #60] Subtotal: $65
00
Grand Total: $876
[Bill #60] Subtotal: $65

If the cashier enters 000, and the subtotal is not 0,
the following error message is displayed, and the prompt
is displayed again:

[Bill #71] Subtotal: $12
000
Please complete the current bill before closing the register.
[Bill #71] Subtotal: $12

If the cashier enters 000, and the subtotal is 0 the day ends:

[Bill #78] Subtotal: $0
000
Closing Register.
Paid Bills: 67
Canceled Bills: 11
Grand Total: $905
Thanks for using the 10x cash register!

And the program exits.

Sample Dialog
-------------
TODO

"""
register = int(raw_input("Welcome to the 10x cash register!\nPlease enter the amount of funds curently deposited in the register: ")) 
help = "Enter a positive number to add to the bill:\nEnter a negtive number to deduct from the bill\nEnter x to cancel the current bill.\nEnter 0 to checkout bill and accept payment.\nEnter 00 to show the cash register status.\nEnter 000 to end the day and exit\nType 'help' for Help."
print help
i = 1
cancelled = 0
bill = 0
while True:
	print "[Bill #%d] Subtotal: $%d." % (i,bill)
	command = raw_input("Please enter a command... ")
	
	if command == "x":
		bill = 0
		cancelled += 1
		continue

	if command == "0":
		register += bill
		print "Bill #%d Payment accepted: %d " % (i, bill)
		print "Grand Total: $%d " % register
		i += 1
		bill = 0
		continue

	if command == "00":
		print "\tGrand Total: $%d" % register
		continue

	if command == "000":
		if bill != 0:
			print "Please complete the current bill before closing the register."
			continue
		print "Closing Register."
		print "Paid Bills: %d" % i
		print "Canceled Bills: %d" % cancelled
		print "Grand Total: $%d" % register
		print "Thanks for using the 10x cash register!"
		break

	bill += int(command)
