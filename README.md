
# HomeCrew

HomeCrew is an organization that provides home services to the common people.They provide many services which are rarely found nowadays such as: watching elder poeple,taking care of kids when no one is home,taking care of pets etc.Here people can order them and also withdraw if they feel they dont need it anymore. 

## Live Link

[HomeCrew](https://homecrew-backend.vercel.app/) is currently deployed on Vercel.Click on the blue link to go to the live website.


## Tech Stack

**FrontEnd Technology:**  Html, CSS, Javascript

**Backend Technology used:**  Python, Django, Django Rest Framework

**Database:**  PostgreSQL


## Authors

- [Asifmahmud436](https://github.com/Asifmahmud436)




## Installation
Actually ,you can just run the requirements.txt file and run the project.But to be 100% sure ,just install the packages below to smoothly run the project on local server. 

Install djangorestframework:

```bash
  pip install djangorestframework
```
Install djangorestframework-authtoken:

```bash
  pip install djangorestframework-authtoken
```
Install dj-rest-auth:

```bash
  pip install dj-rest-auth
```
Install django-cors-headers:

```bash
  pip install django-cors-headers
```
Install pillow:

```bash
  pip install pillow
```
Install requests:

```bash
  pip install requests
```
    
## API Reference

#### Get all services

```http
  GET /api/service/service/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all the services |

#### Get all reviews

```http
  GET /api/service/review/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all the reviews about the service |

#### Get all Ordered items

```http
  Get /api/cart/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get all ordered items |

#### Get all Ordered of a particular client
```http
  Get /api/cart/?client_id=${client_id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | get ordered list of a particular client by client_id |

#### Get all the clients

```http
  GET /api/client/list/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | get the list of all clients |

#### Get client details

```http
  GET /api/client/list/${user_id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | get the client details by user_id |

```http
  POST /api/service/service/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | submit a service as an admin|


#### Login 

```http
  POST /api/client/logout/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | logout as a client |

#### Logout 

```http
  POST /api/client/login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | login as a client |

#### Register

```http
  POST /api/client/register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | register as a client |

#### Order items

```http
  POST /api/cart/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | order items |


#### Cancel Order

```http
  PATCH /api/cart/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | Cancel an order |

#### Edit client details

```http
  PATCH /api/client/list/${user_id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | edit client details by user_id |


#### Deliver Order

```http
  PATCH /api/cart/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | deliver the order as an admin to the client |





## Run Locally

Clone the project

```bash
  git clone https://github.com/Asifmahmud436/homecrew-backend
```

Go to the project directory

```bash
  cd homecrew-backend
```

Install dependencies

```bash
  pip install django
```

Start the server

```bash
  python manage.py runserver
```






## Features

- Live previews
- Fullscreen mode
- Cross platform

## Lessons Learned

After completing this project, I can: 
- Use multiple role base user
- Can sort the services by average rankings
- Deploy Projects on Vercel 
- Use supabase as a site for deploying my PostgreSQL


## Contribution

Contributions are always welcome!

Fork and clone the Project to your own repository.Then create a branch,update the code and send a pull request

Please adhere to this project's `code of conduct`.


## Support

For support, email safaandsafa4@gmail.com or join our discord: https://discord.gg/DaU4QuNM




## 🔗 Connect with me:
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asif-mahmud-3bb1a627a/)


## Feedback

If you have any feedback, please reach out to us at safaandsafa4@gmail.com
