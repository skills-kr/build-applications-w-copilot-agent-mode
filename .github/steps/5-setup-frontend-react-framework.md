## Step 5: 프론트엔드 React 프레임워크 설정, 컴포넌트 업데이트, OctoFit Tracker 앱 시작

> [!NOTE]
> **비하인드 스토리:** 이 실습은 GitHub Copilot의 응답을 안내하는 커스텀 인스트럭션 파일을 사용합니다. 인스트럭션 파일 `.github/instructions/octofit_tracker_react_frontend.instructions.md`에는 React 프레임워크 설정 명령, Bootstrap 통합, 프론트엔드 구조 가이드라인이 포함되어 있으며 Copilot이 이 단계의 코드를 생성할 때 참조합니다.

이 단계에서 다음을 수행합니다:

- octofit-tracker 프론트엔드 React 프레임워크를 설정합니다.
- 다음 컴포넌트를 React 프레임워크에 맞게 업데이트합니다:
  - src/App.js
  - src/index.js
  - src/components/Activities.js
  - src/components/Leaderboard.js
  - src/components/Teams.js
  - src/components/Users.js
  - src/components/Workouts.js
- React 앱을 시작하고 출력을 확인합니다.

GitHub Copilot Chat에 다음 프롬프트를 복사하여 붙여넣고, 프롬프트를 입력하는 곳의 드롭다운에서 "Agent"를 "Ask" 또는 "Edit" 대신 선택합니다.

> [!NOTE]
> - Copilot 에이전트 모드는 대화형이므로 질문을 할 수 있고 여러분도 질문할 수 있습니다.
> - Copilot이 응답할 때까지 잠시 기다린 후 Copilot 에이전트 모드가 제시하는 명령을 실행하려면 Continue 버튼을 누르세요.
> - Copilot 에이전트 모드가 작업을 완료할 때까지 생성 및 업데이트된 파일을 유지하세요.
> - 에이전트 모드는 코드베이스를 평가하고 명령을 실행하며, 코드베이스의 일부를 추가/리팩터링/삭제하고, 실수가 발생하면 자동으로 복구하는 능력을 가지고 있습니다.

**Copilot Chat 창의 `+` 아이콘을 눌러 새 Copilot Chat 세션을 엽니다.**

### :keyboard: 활동: octofit-tracker 프론트엔드 React 프레임워크 설치

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's setup the octofit-tracker frontend React  framework and
> ensure everything is created in the `octofit-tracker/frontend` directory by using `--prefix`
>
> 1. Make sure the the octofit-tracker/frontend directory exists.
> 2. create the react app
> 3. Install react, bootstrap, and react-router-dom
> 4. Import bootstrap css in the src/index.js file.
> 5. Don't change .gitignore file
>```

### :keyboard: 활동: octofit-tracker 프론트엔드 React 컴포넌트 업데이트

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's update the octofit-tracker frontend React components.
>
> - Update the following components to include the React framework to point to the backend REST API:
>   - src/App.js
>   - src/index.js
>   - src/components/Activities.js
>   - src/components/Leaderboard.js
>   - src/components/Teams.js
>   - src/components/Users.js
>   - src/components/Workouts.js
> - In each component replace the fetch url with the codespace url
>   https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/[component]/
>   for the Django rest framework backend.
>   make sure all components are pulling data from the REST api endpoint
>   for display in the REACT frontend
> - Make sure to use the correct port and protocol http or https.
> - Update src/App.js to include the main navigation for all components.
> - Make sure react-router-dom is used for the navigation menu.
> - The react app should show the navigation menu and the components.
> - Update all components to log the fetched data and make them compatible with both paginated (.results) and plain array responses.
> - Add console.log statements to each component to log the fetched data and the REST API endpoints.
> ```

### :keyboard: 활동: React 앱 시작 및 출력 확인

이제 React 애플리케이션을 실제로 실행해 봅시다! 왼쪽 사이드바에서 `Run and Debug` 탭을 선택한 후 **Start Debugging** 아이콘을 누릅니다.

<img alt="Run React Frontend" src="https://github.com/user-attachments/assets/b76a8e82-8435-4cbd-9540-8143756d1c60"  width=30% height=30%>

포트 3000에 대한 React Frontend URL 팝업으로 이동합니다:

<img alt="react-frontend-port" src="https://github.com/user-attachments/assets/a0c8b213-ee5f-46dd-8675-686a7ba0818f" width=30% height=30%>

웹 브라우저에서 열면 다음과 같은 경고가 표시됩니다:

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/cb52d137-e78d-440b-8e9c-c322d7c49b48" width=30% height=30%>

`Continue`를 클릭하면 다음과 비슷하게 표시됩니다:

<img alt="react-frontend-app" src="https://github.com/user-attachments/assets/f7f1a076-c259-49f6-8aa5-9ebcd5f0698d" width=50% height=50%>

### :keyboard: 활동: OctoFit Tracker 앱에 포맷팅, 구조화, 스타일링 추가하기

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's style this like App.css and make it look nice.
>
> - Let's make the App.js and all components javascript files in the app are consistent with the following:
>   - Use bootstrap tables for the data in all javascript components.
>   - Use bootstrap buttons for the buttons.
>   - Use bootstrap headings for the headings.
>   - Use bootstrap links for the links.
>   - Use bootstrap navigation for the navigation menu.
>   - Use bootstrap forms for the forms.
>   - Use bootstrap cards for the cards.
>   - Use bootstrap modals for the modals.
>   - Consistent table layouts for all components data.
>```

### :keyboard: 선택 활동: OctoFit Tracker 앱을 예쁘게 꾸미고 색상 추가하기

> ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Let's style this like App.css and make it look nice.
> 
> -  Edit the App.css file to do the following:
>   - Add some color to the background.
>   - Add some color to the text.
>   - Add some color to the tables.
>   - Add some color to the buttons.
>   - Add some color to the headings.
>   - Add some color to the links.
>   - Add some color to the navigation menu.
> - Add the octofitapp-small logo justified to the left to the app and make it look nice.
> - Add a favicon to the app and make it look nice.
>```

### :keyboard: 선택 활동: 외관을 반복 개선하고 다른 모델 사용해 보기

> [!TIP]
> - 직접 프롬프트를 작성하여 앱의 외관을 변경하고, 기능을 추가하며, 다른 모델을 사용해 보세요.

1. 모든 애플리케이션 컴포넌트의 React 프론트엔드를 만들었으니, 변경사항을 `build-octofit-app` 브랜치에 체크인합니다.

1. 새로운 변경사항이 완료되면 `build-octofit-app` 브랜치에 **커밋**하고 **푸시**합니다.

1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다립니다!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

피드백이 없다면 다음을 확인하세요:

- `build-octofit-app` 브랜치에 다음 파일의 커밋 변경사항이 있고 GitHub에 푸시/동기화되었는지 확인하세요:
  - `octofit-tracker/frontend/src/components/Activities.js`에 `-8000.app.github.dev/api/activities/`가 포함
  - `octofit-tracker/frontend/src/components/Leaderboard.js`에 `-8000.app.github.dev/api/leaderboard/`가 포함
  - `octofit-tracker/frontend/src/components/Teams.js`에 `-8000.app.github.dev/api/teams/`가 포함
  - `octofit-tracker/frontend/src/components/Users.js`에 `-8000.app.github.dev/api/users/`가 포함
  - `octofit-tracker/frontend/src/components/Workouts.js`에 `-8000.app.github.dev/api/workouts/`가 포함
- Mona가 실수를 발견하면 수정하고 다시 푸시하세요. Mona는 필요한 만큼 여러 번 작업을 확인합니다.

</details>
