Public Class TheArtOfGiving
  Inherits System.Windows.Forms.Form

  'declare class-level variables
  Dim totalAmount As Double

  Private Sub TheArtOfGiving_Load(sender As Object, e As EventArgs) Handles MyBase.Load
    totalAmount = 0.00
  End Sub

  Private Sub btnAddDonation_Click(sender As Object, e As EventArgs) Handles btnAddDonation.Click
    Dim amount As Double
    If double.TryParse(txtDonationAmount.Text, amount) Then
      totalAmount += amount
      lblTotalAmount.Text = totalAmount.ToString("C")
    Else
      MessageBox.Show("Input must be numeric")
    EndIf
  End Sub

  Private Sub btnReset_Click(sender As Object, e As EventArgs) Handles btnReset.Click
    totalAmount = 0.00
    lblTotalAmount.Text = totalAmount.ToString("C")
  End Sub

  Private Sub btnSend_Click(sender As Object, e As EventArgs) Handles btnSend.Click
    If totalAmount > 0 Then
      Dim msg As String
      msg = "Sending a donation of {0} to {1}".Format(lblTotalAmount.Text, txtCharityName.Text)
      MessageBox.Show(msg, "Confirmation", MessageBoxButtons.OK, MessageBoxIcon.Information)
    Else
      MessageBox.Show("No donation amount was entered", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
    End If
  End Sub

End Class