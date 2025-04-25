# Hiccup File Management Capabilities

This document provides instructions on how to rebuild the terminator module and test the new file management capabilities added to the Hiccup voice assistant.

## Overview

The Hiccup voice assistant now supports file management operations through natural language voice commands:

- **Create folders**: `create a folder on desktop named projects`
- **Delete files**: `delete file notes.txt on desktop`

## Natural Language Support

Hiccup now understands a wide variety of natural language commands for file management. The system is designed to be flexible and user-friendly, allowing you to express your intent in many different ways:

### Create Folder Commands

The system understands various ways of asking to create a folder:

- `create a folder on desktop named projects`
- `make a folder called projects on desktop`
- `create a folder with name projects in documents`
- `make a folder as backup in downloads`
- `create a folder projects` (defaults to desktop)
- `please create a folder on my desktop named work`
- `could you make a folder called personal in my documents`

### Delete File Commands

Similarly, the system understands various ways of asking to delete a file:

- `delete file notes.txt on desktop`
- `remove file document.txt from desktop`
- `delete file backup.txt` (defaults to desktop)
- `remove the file test.txt in documents`
- `delete my file report.txt in downloads`
- `I want to delete the file old.txt from my desktop`
- `can you remove file temp.txt in my downloads folder`

## Rebuilding the Terminator Module

To rebuild the terminator module with the new file management capabilities, follow these steps:

1. Navigate to the terminator directory:
   ```
   cd terminator
   ```

2. Build the module using maturin:
   ```
   maturin develop
   ```

3. If you want to build for release:
   ```
   maturin build --release
   ```

## Testing the File Management Capabilities

### Automated Testing

Run the automated test script to verify that the file management capabilities work correctly:

```
python test_file_management.py
```

This script will:
1. Simulate various natural language voice commands for creating folders and deleting files
2. Verify that folders are created in the correct locations
3. Report the results of the tests

### Manual Testing

You can also test the file management capabilities manually:

1. Run the Hiccup voice assistant:
   ```
   python -m core.app
   ```

2. Try various natural language commands, such as:
   - `create a folder on desktop named test_folder`
   - `make a folder called another_folder in documents`
   - `delete file test.txt from desktop`
   - `remove the file another.txt in downloads`

3. Check your computer to verify that the folders were created and files were deleted in the correct locations.

## Supported Locations

The file management capabilities support the following standard locations:

- Desktop
- Documents
- Downloads
- Pictures
- Music
- Videos

You can also specify a full path if needed.

## Error Handling

The file management capabilities include error handling for:

- Invalid paths
- Permission issues
- Files/folders that already exist or don't exist
- Invalid command syntax

If an error occurs, the assistant will provide feedback about the error.

## Implementation Details

The file management capabilities are implemented in:

1. **Rust Backend**:
   - `terminator/src/platforms/mod.rs`: Added `create_folder` and `delete_file` methods to the `AccessibilityEngineSync` trait
   - `terminator/src/platforms/windows.rs`: Implemented the `create_folder` and `delete_file` methods for Windows
   - `terminator/src/lib.rs`: Exposed the file management methods to Python

2. **Python Frontend**:
   - `core/hiccup_core.py`: Added methods to parse and execute file management commands with natural language support

## Troubleshooting

If you encounter issues with the file management capabilities:

1. Check that the terminator module was built correctly
2. Verify that you have the necessary permissions to create folders and delete files
3. Check the console output for error messages
4. Try using absolute paths instead of relative paths 