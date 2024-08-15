# Nigeria License Plate Detection and Recognition System (NLPDRS)

## Overview

The Nigeria License Plate Detection and Recognition System (NLPDRS) is an advanced AI-driven tool designed to detect and recognize Nigerian license plates from vehicles in various conditions. Utilizing state-of-the-art deep learning models for detection and PaddleOCR for text extraction, NLPDRS offers a robust solution for license plate recognition. The system is currently in its first version, which includes a feature to identify wanted vehicles by matching their license plate numbers.

## Detection and Recognition Implementation

The NLPDRS captures images or video feeds, uses the custom detection model to identify Nigerian license plates in each frame, and extracts the text from the detected plates. The system employs Ultralytics YOLOv8 for plate detection and PaddleOCR for text extraction, ensuring high accuracy and reliability.

### Key Features:
- **License Plate Detection:** Utilizes a custom-trained YOLOv8 model to accurately detect Nigerian license plates under various conditions.
- **Text Extraction:** Implements PaddleOCR to reliably extract text from detected license plates.
- **Wanted Car Detection:** Allows users to input the license plate number of wanted vehicles, and the system will alert them upon detection.
- **User-Friendly Interface:** Built with Gradio, providing an easy-to-use web interface for testing and interaction.

## Web Interface on Gradio

The NLPDRS features a user-friendly web interface developed with Gradio, enabling users to interact with the system seamlessly. The Gradio interface allows users to:
- **Upload Images or Videos:** Users can upload images or provide live video feeds for the system to process.
- **View Detection Results:** The interface displays detected license plates and the extracted text in real-time.
- **Input Wanted Plate Numbers:** Users can enter the license plate numbers of wanted vehicles, and the system will continuously monitor the inputs and trigger an alert if a match is found.

### How to Use the Gradio Interface:
1. **Access the Interface:** Log in to Hugging Face and access the NLPDRS Gradio interface using the following link: [NLPDRS Gradio Demo](https://huggingface.co/spaces/esssyjr/NLPDRS)
2. **Upload and Detect:** Use the "Upload" button to select an image or video containing vehicles. The system will detect Nigerian license plates and display the results.
3. **Wanted List Alert:** Enter the license plate number of any wanted vehicle in the designated input field. The system will alert you if the wanted plate number is detected.

## Future Improvements

This detection and recognition model has the potential to be extended for various applications beyond the current capabilities, such as:

- **Real-Time Monitoring:** Implementing real-time monitoring features for continuous surveillance and alert generation.
- **Integration with Security Databases:** Linking with national and local security databases for automatic cross-referencing of detected plates.
- **Multi-Language Support:** Enhancing the OCR system to support multiple languages and scripts for broader applicability.

## Collaboration

As a computer vision model developer, I acknowledge my limitations and recognize the importance of collaboration in making projects a reality. While I bring expertise in developing models and algorithms, I understand that collaborative efforts can enhance the scope and impact of projects.

I am open to collaboration on this project and others, leveraging the collective expertise of diverse individuals to overcome challenges and achieve shared goals. Whether you're a fellow developer, data scientist, software developer, domain expert, or enthusiast, I welcome collaboration opportunities to push the boundaries of AI applications.

If you're interested in collaborating or have ideas for potential projects, feel free to reach out.

## Citation

The dataset utilized in this project was provided by EJAZTECH.AI, a company dedicated to gathering local datasets for AI applications, founded by me. We acknowledge their invaluable contribution to the development of this model and other models by providing access to diverse and localized data, which played a crucial role in developing the NLPDRS model. I express my gratitude to EJAZTECH.AI for their commitment to advancing AI research and applications in Nigeria and beyond.

For further inquiries or collaboration opportunities, you can contact the company via their email address:

Email: [ejaztech.ai@gmail.com]

---

Thank you for using the Nigeria License Plate Detection and Recognition System! We look forward to bringing more advanced features in future versions.
