def display_buckets(bucket_8L, bucket_5L, bucket_3L):
    """Displays the current state of the buckets."""
    print("Try to get 4L of water into one of these buckets:")
    for i in range(8, 0, -1):
        print(f'{i}| {"WWWWWW" if bucket_8L >= i else "      "} |        {i}| {"WWWWWW" if bucket_5L >= i else "      "} |        {i}| {"WWWWWW" if bucket_3L >= i else "      "} |')
    print(" +------+         +------+         +------+")
    print("    8L               5L               3L")


def fill(bucket, capacity):
    """Fill the bucket to its full capacity."""
    return capacity


def empty(bucket):
    """Empty the bucket."""
    return 0


def pour(from_bucket, to_bucket, to_capacity):
    """Pour water from one bucket into another."""
    amount_to_pour = min(from_bucket, to_capacity - to_bucket)
    return from_bucket - amount_to_pour, to_bucket + amount_to_pour


def water_bucket_puzzle():
    # Initial amounts of water in the buckets
    bucket_8L = 0
    bucket_5L = 0
    bucket_3L = 0

    # Bucket capacities
    capacity_8L = 8
    capacity_5L = 5
    capacity_3L = 3

    while True:
        display_buckets(bucket_8L, bucket_5L, bucket_3L)

        # Check if any bucket has 4L of water
        if bucket_8L == 4 or bucket_5L == 4 or bucket_3L == 4:
            print("Congratulations! You've solved the puzzle!")
            break

        # Ask the user what to do
        print("\nYou can:")
        print("  (F)ill the bucket")
        print("  (E)mpty the bucket")
        print("  (P)our one bucket into another")
        print("  (Q)uit")
        action = input("> ").lower()

        if action == 'q':
            print("Thanks for playing!")
            break

        # Select a bucket for the action
        bucket_choice = input("Select a bucket 8, 5, 3, or QUIT: ").lower()

        if bucket_choice == 'quit':
            print("Thanks for playing!")
            break

        # Perform the selected action
        if bucket_choice == '8':
            selected_bucket = 8
        elif bucket_choice == '5':
            selected_bucket = 5
        elif bucket_choice == '3':
            selected_bucket = 3
        else:
            print("Invalid bucket choice. Try again.")
            continue

        if action == 'f':
            # Fill the selected bucket
            if selected_bucket == 8:
                bucket_8L = fill(bucket_8L, capacity_8L)
            elif selected_bucket == 5:
                bucket_5L = fill(bucket_5L, capacity_5L)
            elif selected_bucket == 3:
                bucket_3L = fill(bucket_3L, capacity_3L)

        elif action == 'e':
            # Empty the selected bucket
            if selected_bucket == 8:
                bucket_8L = empty(bucket_8L)
            elif selected_bucket == 5:
                bucket_5L = empty(bucket_5L)
            elif selected_bucket == 3:
                bucket_3L = empty(bucket_3L)

        elif action == 'p':
            # Pour one bucket into another
            from_bucket = selected_bucket
            to_bucket = input("Pour into which bucket? (8, 5, 3): ")

            if from_bucket == 8:
                if to_bucket == '5':
                    bucket_8L, bucket_5L = pour(bucket_8L, bucket_5L, capacity_5L)
                elif to_bucket == '3':
                    bucket_8L, bucket_3L = pour(bucket_8L, bucket_3L, capacity_3L)
                else:
                    print("Invalid choice.")
                    continue
            elif from_bucket == 5:
                if to_bucket == '8':
                    bucket_5L, bucket_8L = pour(bucket_5L, bucket_8L, capacity_8L)
                elif to_bucket == '3':
                    bucket_5L, bucket_3L = pour(bucket_5L, bucket_3L, capacity_3L)
                else:
                    print("Invalid choice.")
                    continue
            elif from_bucket == 3:
                if to_bucket == '8':
                    bucket_3L, bucket_8L = pour(bucket_3L, bucket_8L, capacity_8L)
                elif to_bucket == '5':
                    bucket_3L, bucket_5L = pour(bucket_3L, bucket_5L, capacity_5L)
                else:
                    print("Invalid choice.")
                    continue
        else:
            print("Invalid action. Try again.")
            continue


if __name__ == '__main__':
    water_bucket_puzzle()
