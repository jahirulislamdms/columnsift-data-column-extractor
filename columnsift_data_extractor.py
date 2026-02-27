import pandas as pd
from tkinter import Tk, filedialog


APP_NAME = "ColumnSift - Data Column Extractor"


def select_file():
    """Open file dialog to select CSV or Excel file."""
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a CSV or Excel file",
        filetypes=[
            ("CSV files", "*.csv"),
            ("Excel files", "*.xlsx;*.xls")
        ]
    )
    return file_path


def load_file(file_path):
    """Load CSV or Excel file into a pandas DataFrame."""
    try:
        if file_path.lower().endswith(".csv"):
            return pd.read_csv(file_path, on_bad_lines="warn", engine="python")
        elif file_path.lower().endswith((".xlsx", ".xls")):
            return pd.read_excel(file_path)
        else:
            print("❌ Unsupported file type.")
            return None
    except Exception as e:
        print(f"❌ Error reading file:\n{e}")
        return None


def display_columns(df):
    """Display available columns."""
    print("\nAvailable Columns:")
    for idx, column in enumerate(df.columns, start=1):
        print(f"{idx}. {column}")


def preview_column(df, column_name):
    """Show first 5 rows of selected column."""
    print(f"\nPreview of '{column_name}':")
    print("-" * 40)
    print(df[column_name].head(5))
    print("-" * 40)


def export_column(df, column_name):
    """Export selected column to a text file."""
    if df[column_name].isnull().all():
        print(f"⚠ Column '{column_name}' is empty. Nothing exported.")
        return

    output_file = f"{column_name}.txt"
    df[column_name].dropna().to_csv(
        output_file,
        index=False,
        header=False
    )
    print(f"✅ Column exported successfully → {output_file}")


def prompt_column_selection(df):
    """Handle user column selection and export process."""
    columns = df.columns.tolist()

    while True:
        try:
            choice = int(input("\nEnter column number to export: "))
            if not 1 <= choice <= len(columns):
                print("❌ Invalid selection.")
                continue

            selected_column = columns[choice - 1]

            preview_column(df, selected_column)

            confirm = input("Export this column? (y/n): ").strip().lower()
            if confirm == "y":
                export_column(df, selected_column)

            again = input("Extract another column? (y/n): ").strip().lower()
            if again != "y":
                print("\n👋 Exiting ColumnSift.")
                break

        except ValueError:
            print("❌ Please enter a valid number.")
        except Exception as e:
            print(f"❌ Unexpected error:\n{e}")


def main():
    print(f"\n=== {APP_NAME} ===\n")

    file_path = select_file()
    if not file_path:
        print("No file selected. Exiting.")
        return

    print(f"\nProcessing file:\n{file_path}")

    df = load_file(file_path)
    if df is None:
        return

    display_columns(df)
    prompt_column_selection(df)


if __name__ == "__main__":
    main()
