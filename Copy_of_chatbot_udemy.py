{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMQgs+hywx3jtnTb8u7hPIK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/leinac/breastcancerprediction/blob/main/Copy_of_chatbot_udemy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MCIuJeTxmgqi"
      },
      "outputs": [],
      "source": [
        "#!pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# !pip install langchain\n",
        "# !pip install openai\n",
        "# !pip install tiktoken\n",
        "# !pip install faiss-cpu\n",
        "# !pip install pypdf\n",
        "#!pip install langchain_community"
      ],
      "metadata": {
        "id": "bOC4UmmFqne_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n"
      ],
      "metadata": {
        "id": "MiG252EcqeNf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.header(\"My first chatbot\")\n",
        "\n",
        "with st.sidebar:\n",
        "  st.title(\"Your Document\")\n",
        "  file = st.file_uploader(\"upload PDF file and ask question\", type='pdf')\n",
        "\n",
        "  if file is not None:\n",
        "    st.write(file)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "KM6N1fjdrXdW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 110
        },
        "id": "ct3SksTw3O-x",
        "outputId": "19c4752c-49c7-4bc3-8d4e-fb573e2ddf96"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-4-ab06b50267fd>, line 1)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-ab06b50267fd>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    export PATH=/content/copy_of_chatbot_udemy.py:/path/to/streamlit\u001b[0m\n\u001b[0m           ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run Copy of chatbot_udemy.py\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "65NEsONwy8Vq",
        "outputId": "97d3cd4f-e8a5-4cc9-b539-8d7879d51e63"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/bin/bash: line 1: streamlit: command not found\n"
          ]
        }
      ]
    }
  ]
}