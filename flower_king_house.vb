Public Class Giving
    'This class defines methods and fields related to the art of giving
    
    'Fields
    Private _giver As Person
    Private _recipient As Person
    Private _gift As Object
    Private _value As Decimal
    Private _thoughtfulness As Integer
    Private _gratefulness As Integer
    
    'Constructors
    Public Sub New(ByVal giver As Person, ByVal recipient As Person, ByVal gift As Object, ByVal value As Decimal)
        _giver = giver
        _recipient = recipient
        _gift = gift
        _value = value
    End Sub
 
    'Properties
    Public ReadOnly Property Giver As Person
        Get
            Return _giver
        End Get
    End Property
 
    Public ReadOnly Property Recipient As Person
        Get
            Return _recipient
        End Get
    End Property
 
    Public ReadOnly Property Gift As Object
        Get
            Return _gift
        End Get
    End Property
 
    Public ReadOnly Property Value As Decimal
        Get
            Return _value
        End Get
    End Property
 
    Public Property Thoughtfulness As Integer
        Get
            Return _thoughtfulness
        End Get
        Set(value As Integer)
            _thoughtfulness = value
        End Set
    End Property
 
    Public Property Gratefulness As Integer
        Get
            Return _gratefulness
        End Get
        Set(value As Integer)
            _gratefulness = value
        End Set
    End Property
 
    'Methods
    Public Function CalculateReward() As Integer
        'Calculates the reward for giving based on the thoughtfulness and gratefulness
        Return _thoughtfulness * _gratefulness
    End Function
 
    Public Function IsWorthwhile() As Boolean
        'Calculates whether the gift is worthwhile
        If _value > 0 And CalculateReward() > 0 Then
            Return True
        Else
            Return False
        End If
    End Function
 
    Public Overrides Function ToString() As String
        'Returns a string representation of the gift
        Return String.Format("{0} gave a {1} worth {2} to {3}.", _giver.Name, _gift, _value, _recipient.Name)
    End Function
 
End Class