import axios from 'axios'
import {apiURL} from "./API.js"

// 获取课程列表
export async function getCourseList(params){
    const result = await axios.get(apiURL.TTS_Chinese_Course_List+params);
    return result
}

export async function getCourseText(params){
    const result = await axios.get(apiURL.TTS_Chinese_Course_Text+params);
    return result
}
