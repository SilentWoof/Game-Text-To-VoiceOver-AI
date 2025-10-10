# docs/modules.md

# Module Breakdown

## src/

- `capture.py`: Captures active window or full screen  
- `ocr.py`: Crops image using `params.py`, runs OCR  
- `params.py`: Stores resolution and region coordinates  
- `utils.py`: Logging and preprocessing utilities  

## tests/

- `calibrate_region.py`: Draws red box over OCR region  
- `ocr_test.py`: Runs full OCR pipeline and prints text  
- `output/`: Stores calibration preview images  

## docs/

- Architecture, setup, privacy, roadmap, changelog  