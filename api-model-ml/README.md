API DOCUMENTATION

HTTP Request
GET https://capstone-389113.et.r.appspot.com

Endpoint
| Endpoint  |   method  |
| /submit 	|   POST    |

Parameter request
| Parameter |	     Tipe	      |  Wajib  |      Desc     |
|  `file`	  | Jpg, jpeg, png  |   Ya    |  Gambar wajah |

Respons
Contoh respon :
{
	“data” : {
		“confidence” : “64%”,
		“prediction” : “Level_2”
	},
	“isError” : false,
	“message” : “Success”,
	“statusCode” : 200
}

Kode Status
|Kode	|         Status         | 
|200	|         Success        |
|400	| Permintaan tidak valid |

Request
POST /submit
Body:
-	image : [file]
