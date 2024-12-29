from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Basic information about services
services = {
    "website_app_design": "We offer comprehensive website and app design services that are user-friendly and visually appealing.",
    "ui_ux_design": "Our UI/UX design services ensure the best user experience through intuitive design.",
    "seo_services": "Our SEO services help increase your online visibility by optimizing your website for search engines.",
    "digital_marketing": "We provide digital marketing services that help drive traffic and boost sales.",
    "social_media_management": "Our social media management services ensure a consistent and engaging online presence."
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    
    # Greeting response
    if "hello" in user_message.lower() or "hi" in user_message.lower():
        return jsonify({"response": "Hello! How can I assist you today?"})

    # Service Inquiry Response
    elif "services" in user_message.lower():
        return jsonify({"response": "We offer the following services: Website & App Design, UI/UX Design, SEO Services, Digital Marketing, and Social Media Management."})

    # Answer specific service-related queries
    for service, description in services.items():
        if service in user_message.lower():
            return jsonify({"response": description})
        
    # Contact Information
        elif "contact" in user_message.lower() or "phone" in user_message.lower():
            return jsonify({"response": "You can reach us at [6299631203] or email us at [Kashyapankit8877@gmail.com]. We're here to help!"})

    # Feedback collection
        elif "feedback" in user_message.lower():
            return jsonify({"response": "Thank you for your inquiry! Please rate your experience on a scale of 1 to 5."})

    # Appointment scheduling
        elif "schedule" in user_message.lower():
            return jsonify({
        "response": "I'd be happy to assist you with scheduling an appointment. Please provide your preferred date and time."
    })

    # Lead Generation
        elif "lead" in user_message.lower():
            return jsonify({
        "response": "I can help you capture your information. Please provide your name, email, and service interest."
    })

    # Live Chat Option
        elif "live chat" in user_message.lower():
            return jsonify({"response": "I will connect you with a live support agent shortly."})

    # Good Morning
        elif "good morning" in user_message.lower():
            return jsonify({"response": "Good morning! How can I assist you today?"})

    # Thank You
        elif "thank you" in user_message.lower():
            return jsonify({"response": "You're welcome! If you have any more questions, feel free to ask."})

    # Help Assistant
        elif "help" in user_message.lower() or "assistant" in user_message.lower():
            return jsonify({"response": "How can I assist you today? Feel free to ask any questions!"})

    # Company Website
        elif "website" in user_message.lower():
            return jsonify({"response": "You can visit our company website at [VaishaliTech.in]. Feel free to explore our services!"})
        
    # Location Inquiry
        elif "location" in user_message.lower() or "address" in user_message.lower():
            return jsonify({"response": "Our office is located at [Bellandur , Bengaluru 560037]. We look forward to seeing you!"})
        
    # Refund or Cancellation Policy
        elif "refund" in user_message.lower() or "cancel" in user_message.lower():
            return jsonify({"response": "Please visit our Refund and Cancellation Policy page on the website, or let me know how I can assist you further."})
        
    # Product Information
        elif "product" in user_message.lower() or "details" in user_message.lower():
            return jsonify({"response": "Can you please specify the product you're looking for? I'll provide detailed information."})

    # Default response for unrecognized messages
    else:
        return jsonify({"response": "I'm sorry, I didn't quite understand that. Could you please rephrase?"})


if __name__ == '__main__':
    app.run(debug=True)

