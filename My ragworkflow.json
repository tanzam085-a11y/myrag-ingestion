{
  "name": "My ragworkflow",
  "nodes": [
    {
      "parameters": {
        "formTitle": "Load File  To ingest",
        "formFields": {
          "values": [
            {
              "fieldLabel": "add file here",
              "fieldType": "file"
            },
            {
              "fieldLabel": "Add reference"
            }
          ]
        },
        "options": {}
      },
      "id": "e1e1c217-cec7-4b71-8cd1-a9b29b058382",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.6,
      "position": [
        0,
        0
      ],
      "webhookId": "64da1ebc-aa0a-4626-9d9c-f14e72c9fa72"
    },
    {
      "parameters": {
        "mode": "insert",
        "qdrantCollection": {
          "__rl": true,
          "mode": "list",
          "value": "my-chatbot"
        },
        "embeddingBatchSize": 100,
        "options": {}
      },
      "id": "d0ae1f14-caa2-41f4-9c52-9a0c8cf9ef33",
      "name": "Qdrant Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreQdrant",
      "typeVersion": 1.3,
      "position": [
        224,
        0
      ],
      "credentials": {
        "qdrantApi": {
          "id": "VWPvUlIGO7HYAMZI",
          "name": "Qdrant account"
        }
      }
    },
    {
      "parameters": {},
      "id": "9b88ad0b-08d1-4dc8-bcfb-3f1466723985",
      "name": "Embeddings Google Gemini",
      "type": "@n8n/n8n-nodes-langchain.embeddingsGoogleGemini",
      "typeVersion": 1,
      "position": [
        224,
        176
      ],
      "credentials": {
        "googlePalmApi": {
          "id": "3woiRsMOj2cS43Xy",
          "name": "Google Gemini(PaLM) Api account"
        }
      }
    },
    {
      "parameters": {
        "textSplittingMode": "custom",
        "options": {}
      },
      "id": "c03b5452-2405-4461-ae03-27617ff70914",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "typeVersion": 1.1,
      "position": [
        384,
        160
      ]
    },
    {
      "parameters": {
        "chunkSize": 400,
        "chunkOverlap": 100,
        "options": {}
      },
      "id": "d1219d79-99c0-4298-9feb-fb5978424498",
      "name": "Recursive Character Text Splitter",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "typeVersion": 1,
      "position": [
        400,
        336
      ]
    },
    {
      "parameters": {
        "content": "rag ingestion process",
        "height": 640,
        "width": 864,
        "color": "#995656"
      },
      "id": "5dac97d8-0ec5-402a-9386-51cfcc3992f7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [
        -144,
        -64
      ]
    },
    {
      "parameters": {
        "content": "chat model",
        "height": 608,
        "width": 672,
        "color": 6
      },
      "id": "97f60f09-dbbf-4710-b445-d3d31ea76480",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [
        -864,
        -32
      ]
    },
    {
      "parameters": {
        "options": {
          "responseMode": "lastNode"
        }
      },
      "id": "dfe90fc5-0744-4328-9cdd-c07be1d4bfba",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "typeVersion": 1.4,
      "position": [
        -720,
        80
      ],
      "webhookId": "3a901b5a-627d-446d-90dd-94f7adbb38de"
    },
    {
      "parameters": {
        "options": {
          "systemMessage": "You are a knowledge-base assistant. For EVERY user question, you MUST first call the \"Qdrant Vector Store1\" retrieval tool to search the knowledge base, then answer using only the information it returns. Do not answer from your own general knowledge. If the retrieval tool returns nothing relevant, reply that you could not find the answer in the provided documents. When relevant, cite the reference/source from the retrieved content.",
          "enableStreaming": true
        }
      },
      "id": "50c6ef15-4c00-488b-b081-8fa2fca1684d",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 3.1,
      "position": [
        -560,
        80
      ],
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "08320891-f1d6-464f-9669-7afebbd25377",
      "name": "Google Gemini Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "typeVersion": 1.1,
      "position": [
        -624,
        304
      ],
      "credentials": {
        "googlePalmApi": {
          "id": "3woiRsMOj2cS43Xy",
          "name": "Google Gemini(PaLM) Api account"
        }
      }
    },
    {
      "parameters": {},
      "id": "ed8e31ff-1739-4c4a-a0c2-1c30c2a8c816",
      "name": "Simple Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1.4,
      "position": [
        -512,
        336
      ]
    },
    {
      "parameters": {
        "mode": "retrieve-as-tool",
        "toolDescription": "use this tool to fetch data knowledge from the database",
        "qdrantCollection": {
          "__rl": true,
          "mode": "list",
          "value": "my-chatbot"
        },
        "options": {}
      },
      "id": "728a5a07-2074-4c9a-8539-dc36191aa6b3",
      "name": "Qdrant Vector Store1",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreQdrant",
      "typeVersion": 1.3,
      "position": [
        -400,
        320
      ],
      "credentials": {
        "qdrantApi": {
          "id": "VWPvUlIGO7HYAMZI",
          "name": "Qdrant account"
        }
      }
    },
    {
      "parameters": {},
      "id": "cd540b42-5341-47f4-ae49-4c7e4d259335",
      "name": "Embeddings Google Gemini1",
      "type": "@n8n/n8n-nodes-langchain.embeddingsGoogleGemini",
      "typeVersion": 1,
      "position": [
        -368,
        512
      ],
      "credentials": {
        "googlePalmApi": {
          "id": "3woiRsMOj2cS43Xy",
          "name": "Google Gemini(PaLM) Api account"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "On form submission": {
      "main": [
        [
          {
            "node": "Qdrant Vector Store",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings Google Gemini": {
      "ai_embedding": [
        [
          {
            "node": "Qdrant Vector Store",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Default Data Loader": {
      "ai_document": [
        [
          {
            "node": "Qdrant Vector Store",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Recursive Character Text Splitter": {
      "ai_textSplitter": [
        [
          {
            "node": "Default Data Loader",
            "type": "ai_textSplitter",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Simple Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Qdrant Vector Store1": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings Google Gemini1": {
      "ai_embedding": [
        [
          {
            "node": "Qdrant Vector Store1",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        []
      ]
    }
  },
  "active": true,
  "settings": {
    "executionOrder": "v1",
    "binaryMode": "separate",
    "timeSavedMode": "fixed",
    "timezone": "Asia/Singapore",
    "saveDataErrorExecution": "all",
    "callerPolicy": "workflowsFromSameOwner",
    "availableInMCP": false
  },
  "versionId": "56cea23c-a667-4a34-a303-3e4a1bd0a1a8",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "1b3501fd34282347eecdcd1e9a3badcf2c4360fa2ccdd9de5f0d745b401ba6a9"
  },
  "nodeGroups": [],
  "id": "oHm3Ct0TSkyMBE6N",
  "tags": []
}