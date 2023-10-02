from angel.angel import Angel
import angel.command as ac


# speech engin configuration
angel = Angel(name= "Angel")


if __name__ == "__main__":
    while True:
        query = ac.command()
        angel.listen(query)