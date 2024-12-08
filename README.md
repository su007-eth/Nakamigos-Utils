# Nakamigos Utils

This is an unofficial Nakamigos resource and tool library, including the original 20,000 Nakamigos PNG images, pixel data, ExcelNakamigos, and more. The image resources are sourced from [https://github.com/linxinglu/nakamigos-unofficial](https://github.com/linxinglu/nakamigos-unofficial).

## Nakamigos Resources

### 1. Original Images (20k PNG)
- **Location:** `data/images/`
- **Sizes:** Available in 2000×2000 pixels and 24×24 pixels
- **File Naming:** `0.png`, `1.png`, `2.png`, …, `19999.png`

### 2. Pixels Data
- **Location:** `data/pixel_data/`
- **Formats:** CSV and TXT
- **Details:**
  - Contains 20,000 lines, each corresponding to the pixel values of one image (24×24 = 576 pixels)
  - Each pixel value is represented in 8-bit hexadecimal RGBA format: `RRGGBBAA`
  - Extracted using the `src/get_pixels.py` tool from the 20k PNG images

## ExcelNakamigos

### File Structure:
- **File:** `excel/ExcelNakamigos.xlsm`
- **Requirements:** Ensure macros are enabled
- **Features:**
  - **"Data" Worksheet:** Stores pixel data
  - **24×24 Display Grid:** Used to view NFTs
  - **Named References:**
    - `NFT_NUMBER`: The NFT ID to view
    - `NFT_START_NUM`: The starting ID of the NFT collection

### How to Draw Different NFTs:
1. **Modify the NFT ID:**
   - Change the value of `NFT ID` and click the 'Draw' button. The grid will automatically fill with colors based on the image's pixel values.
2. **Navigate Through NFTs:**
   - Use the up and down arrows to switch between different NFTs.
3. **Pixel Representation:**
   - Each cell's color in the grid represents a single pixel of the NFT.

## Contribution

Contributions are welcome! You can contribute in the following ways:
1. **Add New Tools or Utilities**
2. **Improve Existing Code**
3. **Add Documentation**
4. **Report Issues**

## License

This is an unofficial tool library. All Nakamigos images and related content are owned by their respective owners.

# Acknowledgements
- Image resources sourced from [Nakamigos Unofficial Repository](https://github.com/linxinglu/nakamigos-unofficial)

# Contact

For any questions or suggestions, please open an issue or contact the repository maintainer.

---

*This project is not affiliated with or endorsed by the official Nakamigos team.*