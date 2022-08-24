<h1>HOW TO RUN</h1>
<br>
<h2>아나콘다 환경설정</h2>
<br>
<p>nevr_fastapi_server.yaml파일 prefix부분 콘다 가상환경 생성하고자 하는곳으로 지정</p>
<p>conda env create -f nevr_fastapi_server.yaml</p>
<br>
<h2>DB설정</h2>
<p>database_config폴더의 sql파일 참조하여 db구성</p>
<p>config폴더의 Settings클래스 로컬 db에 맞게 설정</p>
<br>
<h2>to run server</h2>
<br>
<p>uvicorn main:app --reload</p>
<br>
<h2>to run test</h2>
<br>
<p>python -m pytest</p>
<br>
<h2>api 명세서(swagger)링크= https://http://127.0.0.1:8000/docs</h2>
