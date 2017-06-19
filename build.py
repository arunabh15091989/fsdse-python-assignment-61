def solution(list_of_nums):
    """Enter Code Here"""
    Even = []
    Even = filter(lambda x: x%2==0 , list_of_nums)
    Odd = []
    Odd = filter(lambda x: x%2!=0, list_of_nums)
    return {'EVEN':len(Even),'ODD':len(Odd)}
