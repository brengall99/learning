def count_errors(file_path: str):
    error_count = 0

    try: 
        with open(file_path, 'r') as f:
            for line in f: 
                if "error" in line.lower():
                    error_count += 1
        
        return error_count
    
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
        return -1
    except Exception as e: 
        print(f"An unexpected error occured: {e}")
        return -1

if __name__ == "__main__":
    log_file_path = "example.log"

    # You can create a dummy file for testing purposes:
    with open(log_file_path, "w") as f:
        f.write("INFO: Application started.\n")
        f.write("WARNING: Database connection slow.\n")
        f.write("ERROR: Failed to write to disk. Access denied.\n")
        f.write("DEBUG: User logged in.\n")
        f.write("Error: A syntax error occurred.\n")
        f.write("WARNING: Low memory detected.\n")
        f.write("CRITICAL: Server is down.\n")

    total_errors = count_errors(log_file_path)

    if total_errors != -1:
        print(f"\nAnalysis of '{log_file_path}':")
        print(f"Total number of errors found: {total_errors}")
