from django import forms


class ReviewForm(forms.Form):
    """
    Form for reviewing a book
    """

    if_favourite = forms.BooleanField(
        label="Favourite?",
        help_text="In your top 100 books of all time?",
        required=False,
    )

    review = forms.CharField(
        widget=forms.Textarea,
        min_length=10,
        error_messages={
            'required': 'Please enter your review',
            'min_length': 'Please write at least 10 characters (you have written %(show_value)s)'
        }
    )