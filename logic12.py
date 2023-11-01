def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool:  
    """
    return  a>9 and a<100 and a%10==a//10
print(main(32))
print(main(22)) 