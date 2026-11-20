def main():
    def top_5_grades(grades):
        result = sorted(grades, reverse=True)
        return result[:5]

    def bottom_10_grades(grades):
        result = sorted(grades, reverse=False)
        return result[:10]

    def get_sorted_n_grades(grades, n, top=True):
        result = sorted(grades, reverse=top)
        return result[:n]

    grades = [80, 70, 35, 78, 99, 67, 90, 74, 31, 54, 96, 20, 74, 35]
    top_5_grades(grades)
    print(grades, 'original')

    print(top_5_grades(grades))
    print(bottom_10_grades(grades))

    print(get_sorted_n_grades(grades, 5, True))
    print(get_sorted_n_grades(grades, 3, False))


if __name__ == '__main__':
    main()
