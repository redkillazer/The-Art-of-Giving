Public Class Form1 

Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load 

End Sub 

Private Sub btnGive_Click(sender As Object, e As EventArgs) Handles btnGive.Click 

Dim intOption As Integer 

intOption = InputBox("Please select an option: 
1. Make a Donation 
2. Donate a Service 
3. Give of Your Time ") 

Select Case intOption 

Case 1 

Dim intAmount As Integer 

intAmount = InputBox("Please enter an amount that you would like to donate:") 

If intAmount > 0 Then 

MsgBox("Thank you for your generous donation. Your contribution will be put to good use.") 

Else 

MsgBox("It appears that you have not made a donation. Please consider donating in the future.") 

End If 

Case 2 

Dim strService As String 

strService = InputBox("Please enter a service that you would like to donate:") 

If strService <> "" Then 

MsgBox("Thank you for your generous donation of the service. Your contribution will be put to good use.") 

Else 

MsgBox("It appears that you have not made a donation. Please consider donating in the future.") 

End If 

Case 3 

Dim intTime As Integer 

intTime = InputBox("Please enter the amount of time (in hours) that you would like to donate:") 

If intTime > 0 Then 

MsgBox("Thank you for your generous donation of time. Your contribution will be put to good use.") 

Else 

MsgBox("It appears that you have not made a donation. Please consider donating in the future.") 

End If 

End Select 

End Sub

End Class