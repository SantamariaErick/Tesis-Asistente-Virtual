using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;
using UnityEngine.UI;

public class ViewModel : MonoBehaviour
{
    public Button btnMic;
    public Button btnSend;

    public InputField inpQuestion;

    private void Start() {

        btnMic = GameObject.Find("MicBoton").GetComponent<Button>();
        btnSend = GameObject.Find("EnvBoton").GetComponent<Button>();
        inpQuestion = GameObject.Find("EntradaTxt").GetComponent<InputField>();

        btnMic.onClick.AddListener(BtnMicClick);
        btnSend.onClick.AddListener(BtnSenClick);

        ShowBtnSend(false);
    }

    public void ShowBtnMic(bool active)
    {
        btnMic.gameObject.SetActive(active); 
    }

    public void ShowBtnSend(bool active)
    {
        btnSend.gameObject.SetActive(active);
    }

    public void BtnMicClick()
    {
        UnityEngine.Debug.Log("Send button microphone");
    }
    public void BtnSenClick()
        
    {
        //GameObject inpQuestion = GameObject.Find("EntradaTxt");
        UnityEngine.Debug.Log("Send button send");
        UnityEngine.Debug.Log("Texto enviado "+ inpQuestion.text);
    }

    public void Input_Changed(string text) 
    {
        ShowBtnMic(false);
        ShowBtnSend(true);


        if (!string.IsNullOrEmpty(text))
        {
            UnityEngine.Debug.Log("Texto ingresado: " + text);
        }
        else
        {
            UnityEngine.Debug.Log("No se ingresó texto.");
        }
    }

}
