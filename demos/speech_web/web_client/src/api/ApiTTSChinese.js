import axios from 'axios'
import {apiURL} from "./API.js"

// 获取课程列表
export async function getCourseList(){
    const result = await axios.get(apiURL.TTS_Chinese_Course_List);
    return result
}

export async function getCourseText(params){
    const result = await axios.get(apiURL.TTS_Chinese_Course_Text+params);
    return result
}
